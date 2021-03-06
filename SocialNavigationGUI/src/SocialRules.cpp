//
// Copyright (c) ZeroC, Inc. All rights reserved.
//
//
// Ice version 3.7.3
//
// <auto-generated>
//
// Generated from file `SocialRules.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

#include <SocialRules.h>
#include <IceUtil/PushDisableWarnings.h>
#include <Ice/LocalException.h>
#include <Ice/ValueFactory.h>
#include <Ice/OutgoingAsync.h>
#include <Ice/InputStream.h>
#include <Ice/OutputStream.h>
#include <IceUtil/PopDisableWarnings.h>

#if defined(_MSC_VER)
#   pragma warning(disable:4458) // declaration of ... hides class member
#elif defined(__clang__)
#   pragma clang diagnostic ignored "-Wshadow"
#elif defined(__GNUC__)
#   pragma GCC diagnostic ignored "-Wshadow"
#endif

#ifndef ICE_IGNORE_VERSION
#   if ICE_INT_VERSION / 100 != 307
#       error Ice version mismatch!
#   endif
#   if ICE_INT_VERSION % 100 >= 50
#       error Beta header file detected
#   endif
#   if ICE_INT_VERSION % 100 < 3
#       error Ice patch level mismatch!
#   endif
#endif

#ifdef ICE_CPP11_MAPPING // C++11 mapping

namespace
{

const ::std::string iceC_RoboCompSocialRules_SocialRules_ids[2] =
{
    "::Ice::Object",
    "::RoboCompSocialRules::SocialRules"
};
const ::std::string iceC_RoboCompSocialRules_SocialRules_ops[] =
{
    "ice_id",
    "ice_ids",
    "ice_isA",
    "ice_ping",
    "objectsChanged",
    "personalSpacesChanged"
};
const ::std::string iceC_RoboCompSocialRules_SocialRules_objectsChanged_name = "objectsChanged";
const ::std::string iceC_RoboCompSocialRules_SocialRules_personalSpacesChanged_name = "personalSpacesChanged";

}

bool
RoboCompSocialRules::SocialRules::ice_isA(::std::string s, const ::Ice::Current&) const
{
    return ::std::binary_search(iceC_RoboCompSocialRules_SocialRules_ids, iceC_RoboCompSocialRules_SocialRules_ids + 2, s);
}

::std::vector<::std::string>
RoboCompSocialRules::SocialRules::ice_ids(const ::Ice::Current&) const
{
    return ::std::vector<::std::string>(&iceC_RoboCompSocialRules_SocialRules_ids[0], &iceC_RoboCompSocialRules_SocialRules_ids[2]);
}

::std::string
RoboCompSocialRules::SocialRules::ice_id(const ::Ice::Current&) const
{
    return ice_staticId();
}

const ::std::string&
RoboCompSocialRules::SocialRules::ice_staticId()
{
    static const ::std::string typeId = "::RoboCompSocialRules::SocialRules";
    return typeId;
}

/// \cond INTERNAL
bool
RoboCompSocialRules::SocialRules::_iceD_objectsChanged(::IceInternal::Incoming& inS, const ::Ice::Current& current)
{
    _iceCheckMode(::Ice::OperationMode::Normal, current.mode);
    auto istr = inS.startReadParams();
    SRObjectSeq iceP_objectsAffordances;
    istr->readAll(iceP_objectsAffordances);
    inS.endReadParams();
    this->objectsChanged(::std::move(iceP_objectsAffordances), current);
    inS.writeEmptyParams();
    return true;
}
/// \endcond

/// \cond INTERNAL
bool
RoboCompSocialRules::SocialRules::_iceD_personalSpacesChanged(::IceInternal::Incoming& inS, const ::Ice::Current& current)
{
    _iceCheckMode(::Ice::OperationMode::Normal, current.mode);
    auto istr = inS.startReadParams();
    ::RoboCompSocialNavigationGaussian::SNGPolylineSeq iceP_intimateSpaces;
    ::RoboCompSocialNavigationGaussian::SNGPolylineSeq iceP_personalSpaces;
    ::RoboCompSocialNavigationGaussian::SNGPolylineSeq iceP_socialSpaces;
    istr->readAll(iceP_intimateSpaces, iceP_personalSpaces, iceP_socialSpaces);
    inS.endReadParams();
    this->personalSpacesChanged(::std::move(iceP_intimateSpaces), ::std::move(iceP_personalSpaces), ::std::move(iceP_socialSpaces), current);
    inS.writeEmptyParams();
    return true;
}
/// \endcond

/// \cond INTERNAL
bool
RoboCompSocialRules::SocialRules::_iceDispatch(::IceInternal::Incoming& in, const ::Ice::Current& current)
{
    ::std::pair<const ::std::string*, const ::std::string*> r = ::std::equal_range(iceC_RoboCompSocialRules_SocialRules_ops, iceC_RoboCompSocialRules_SocialRules_ops + 6, current.operation);
    if(r.first == r.second)
    {
        throw ::Ice::OperationNotExistException(__FILE__, __LINE__, current.id, current.facet, current.operation);
    }

    switch(r.first - iceC_RoboCompSocialRules_SocialRules_ops)
    {
        case 0:
        {
            return _iceD_ice_id(in, current);
        }
        case 1:
        {
            return _iceD_ice_ids(in, current);
        }
        case 2:
        {
            return _iceD_ice_isA(in, current);
        }
        case 3:
        {
            return _iceD_ice_ping(in, current);
        }
        case 4:
        {
            return _iceD_objectsChanged(in, current);
        }
        case 5:
        {
            return _iceD_personalSpacesChanged(in, current);
        }
        default:
        {
            assert(false);
            throw ::Ice::OperationNotExistException(__FILE__, __LINE__, current.id, current.facet, current.operation);
        }
    }
}
/// \endcond

/// \cond INTERNAL
void
RoboCompSocialRules::SocialRulesPrx::_iceI_objectsChanged(const ::std::shared_ptr<::IceInternal::OutgoingAsyncT<void>>& outAsync, const SRObjectSeq& iceP_objectsAffordances, const ::Ice::Context& context)
{
    outAsync->invoke(iceC_RoboCompSocialRules_SocialRules_objectsChanged_name, ::Ice::OperationMode::Normal, ::Ice::FormatType::DefaultFormat, context,
        [&](::Ice::OutputStream* ostr)
        {
            ostr->writeAll(iceP_objectsAffordances);
        },
        nullptr);
}
/// \endcond

/// \cond INTERNAL
void
RoboCompSocialRules::SocialRulesPrx::_iceI_personalSpacesChanged(const ::std::shared_ptr<::IceInternal::OutgoingAsyncT<void>>& outAsync, const ::RoboCompSocialNavigationGaussian::SNGPolylineSeq& iceP_intimateSpaces, const ::RoboCompSocialNavigationGaussian::SNGPolylineSeq& iceP_personalSpaces, const ::RoboCompSocialNavigationGaussian::SNGPolylineSeq& iceP_socialSpaces, const ::Ice::Context& context)
{
    outAsync->invoke(iceC_RoboCompSocialRules_SocialRules_personalSpacesChanged_name, ::Ice::OperationMode::Normal, ::Ice::FormatType::DefaultFormat, context,
        [&](::Ice::OutputStream* ostr)
        {
            ostr->writeAll(iceP_intimateSpaces, iceP_personalSpaces, iceP_socialSpaces);
        },
        nullptr);
}
/// \endcond

/// \cond INTERNAL
::std::shared_ptr<::Ice::ObjectPrx>
RoboCompSocialRules::SocialRulesPrx::_newInstance() const
{
    return ::IceInternal::createProxy<SocialRulesPrx>();
}
/// \endcond

const ::std::string&
RoboCompSocialRules::SocialRulesPrx::ice_staticId()
{
    return SocialRules::ice_staticId();
}

namespace Ice
{
}

#else // C++98 mapping

namespace
{

const ::std::string iceC_RoboCompSocialRules_SocialRules_objectsChanged_name = "objectsChanged";

const ::std::string iceC_RoboCompSocialRules_SocialRules_personalSpacesChanged_name = "personalSpacesChanged";

}

/// \cond INTERNAL
::IceProxy::Ice::Object* ::IceProxy::RoboCompSocialRules::upCast(SocialRules* p) { return p; }

void
::IceProxy::RoboCompSocialRules::_readProxy(::Ice::InputStream* istr, ::IceInternal::ProxyHandle< SocialRules>& v)
{
    ::Ice::ObjectPrx proxy;
    istr->read(proxy);
    if(!proxy)
    {
        v = 0;
    }
    else
    {
        v = new SocialRules;
        v->_copyFrom(proxy);
    }
}
/// \endcond

::Ice::AsyncResultPtr
IceProxy::RoboCompSocialRules::SocialRules::_iceI_begin_objectsChanged(const ::RoboCompSocialRules::SRObjectSeq& iceP_objectsAffordances, const ::Ice::Context& context, const ::IceInternal::CallbackBasePtr& del, const ::Ice::LocalObjectPtr& cookie, bool sync)
{
    ::IceInternal::OutgoingAsyncPtr result = new ::IceInternal::CallbackOutgoing(this, iceC_RoboCompSocialRules_SocialRules_objectsChanged_name, del, cookie, sync);
    try
    {
        result->prepare(iceC_RoboCompSocialRules_SocialRules_objectsChanged_name, ::Ice::Normal, context);
        ::Ice::OutputStream* ostr = result->startWriteParams(::Ice::DefaultFormat);
        ostr->write(iceP_objectsAffordances);
        result->endWriteParams();
        result->invoke(iceC_RoboCompSocialRules_SocialRules_objectsChanged_name);
    }
    catch(const ::Ice::Exception& ex)
    {
        result->abort(ex);
    }
    return result;
}

void
IceProxy::RoboCompSocialRules::SocialRules::end_objectsChanged(const ::Ice::AsyncResultPtr& result)
{
    _end(result, iceC_RoboCompSocialRules_SocialRules_objectsChanged_name);
}

::Ice::AsyncResultPtr
IceProxy::RoboCompSocialRules::SocialRules::_iceI_begin_personalSpacesChanged(const ::RoboCompSocialNavigationGaussian::SNGPolylineSeq& iceP_intimateSpaces, const ::RoboCompSocialNavigationGaussian::SNGPolylineSeq& iceP_personalSpaces, const ::RoboCompSocialNavigationGaussian::SNGPolylineSeq& iceP_socialSpaces, const ::Ice::Context& context, const ::IceInternal::CallbackBasePtr& del, const ::Ice::LocalObjectPtr& cookie, bool sync)
{
    ::IceInternal::OutgoingAsyncPtr result = new ::IceInternal::CallbackOutgoing(this, iceC_RoboCompSocialRules_SocialRules_personalSpacesChanged_name, del, cookie, sync);
    try
    {
        result->prepare(iceC_RoboCompSocialRules_SocialRules_personalSpacesChanged_name, ::Ice::Normal, context);
        ::Ice::OutputStream* ostr = result->startWriteParams(::Ice::DefaultFormat);
        ostr->write(iceP_intimateSpaces);
        ostr->write(iceP_personalSpaces);
        ostr->write(iceP_socialSpaces);
        result->endWriteParams();
        result->invoke(iceC_RoboCompSocialRules_SocialRules_personalSpacesChanged_name);
    }
    catch(const ::Ice::Exception& ex)
    {
        result->abort(ex);
    }
    return result;
}

void
IceProxy::RoboCompSocialRules::SocialRules::end_personalSpacesChanged(const ::Ice::AsyncResultPtr& result)
{
    _end(result, iceC_RoboCompSocialRules_SocialRules_personalSpacesChanged_name);
}

/// \cond INTERNAL
::IceProxy::Ice::Object*
IceProxy::RoboCompSocialRules::SocialRules::_newInstance() const
{
    return new SocialRules;
}
/// \endcond

const ::std::string&
IceProxy::RoboCompSocialRules::SocialRules::ice_staticId()
{
    return ::RoboCompSocialRules::SocialRules::ice_staticId();
}

RoboCompSocialRules::SocialRules::~SocialRules()
{
}

/// \cond INTERNAL
::Ice::Object* RoboCompSocialRules::upCast(SocialRules* p) { return p; }

/// \endcond

namespace
{
const ::std::string iceC_RoboCompSocialRules_SocialRules_ids[2] =
{
    "::Ice::Object",
    "::RoboCompSocialRules::SocialRules"
};

}

bool
RoboCompSocialRules::SocialRules::ice_isA(const ::std::string& s, const ::Ice::Current&) const
{
    return ::std::binary_search(iceC_RoboCompSocialRules_SocialRules_ids, iceC_RoboCompSocialRules_SocialRules_ids + 2, s);
}

::std::vector< ::std::string>
RoboCompSocialRules::SocialRules::ice_ids(const ::Ice::Current&) const
{
    return ::std::vector< ::std::string>(&iceC_RoboCompSocialRules_SocialRules_ids[0], &iceC_RoboCompSocialRules_SocialRules_ids[2]);
}

const ::std::string&
RoboCompSocialRules::SocialRules::ice_id(const ::Ice::Current&) const
{
    return ice_staticId();
}

const ::std::string&
RoboCompSocialRules::SocialRules::ice_staticId()
{
#ifdef ICE_HAS_THREAD_SAFE_LOCAL_STATIC
    static const ::std::string typeId = "::RoboCompSocialRules::SocialRules";
    return typeId;
#else
    return iceC_RoboCompSocialRules_SocialRules_ids[1];
#endif
}

/// \cond INTERNAL
bool
RoboCompSocialRules::SocialRules::_iceD_objectsChanged(::IceInternal::Incoming& inS, const ::Ice::Current& current)
{
    _iceCheckMode(::Ice::Normal, current.mode);
    ::Ice::InputStream* istr = inS.startReadParams();
    SRObjectSeq iceP_objectsAffordances;
    istr->read(iceP_objectsAffordances);
    inS.endReadParams();
    this->objectsChanged(iceP_objectsAffordances, current);
    inS.writeEmptyParams();
    return true;
}
/// \endcond

/// \cond INTERNAL
bool
RoboCompSocialRules::SocialRules::_iceD_personalSpacesChanged(::IceInternal::Incoming& inS, const ::Ice::Current& current)
{
    _iceCheckMode(::Ice::Normal, current.mode);
    ::Ice::InputStream* istr = inS.startReadParams();
    ::RoboCompSocialNavigationGaussian::SNGPolylineSeq iceP_intimateSpaces;
    ::RoboCompSocialNavigationGaussian::SNGPolylineSeq iceP_personalSpaces;
    ::RoboCompSocialNavigationGaussian::SNGPolylineSeq iceP_socialSpaces;
    istr->read(iceP_intimateSpaces);
    istr->read(iceP_personalSpaces);
    istr->read(iceP_socialSpaces);
    inS.endReadParams();
    this->personalSpacesChanged(iceP_intimateSpaces, iceP_personalSpaces, iceP_socialSpaces, current);
    inS.writeEmptyParams();
    return true;
}
/// \endcond

namespace
{
const ::std::string iceC_RoboCompSocialRules_SocialRules_all[] =
{
    "ice_id",
    "ice_ids",
    "ice_isA",
    "ice_ping",
    "objectsChanged",
    "personalSpacesChanged"
};

}

/// \cond INTERNAL
bool
RoboCompSocialRules::SocialRules::_iceDispatch(::IceInternal::Incoming& in, const ::Ice::Current& current)
{
    ::std::pair<const ::std::string*, const ::std::string*> r = ::std::equal_range(iceC_RoboCompSocialRules_SocialRules_all, iceC_RoboCompSocialRules_SocialRules_all + 6, current.operation);
    if(r.first == r.second)
    {
        throw ::Ice::OperationNotExistException(__FILE__, __LINE__, current.id, current.facet, current.operation);
    }

    switch(r.first - iceC_RoboCompSocialRules_SocialRules_all)
    {
        case 0:
        {
            return _iceD_ice_id(in, current);
        }
        case 1:
        {
            return _iceD_ice_ids(in, current);
        }
        case 2:
        {
            return _iceD_ice_isA(in, current);
        }
        case 3:
        {
            return _iceD_ice_ping(in, current);
        }
        case 4:
        {
            return _iceD_objectsChanged(in, current);
        }
        case 5:
        {
            return _iceD_personalSpacesChanged(in, current);
        }
        default:
        {
            assert(false);
            throw ::Ice::OperationNotExistException(__FILE__, __LINE__, current.id, current.facet, current.operation);
        }
    }
}
/// \endcond

/// \cond STREAM
void
RoboCompSocialRules::SocialRules::_iceWriteImpl(::Ice::OutputStream* ostr) const
{
    ostr->startSlice(ice_staticId(), -1, true);
    ::Ice::StreamWriter< SocialRules, ::Ice::OutputStream>::write(ostr, *this);
    ostr->endSlice();
}

void
RoboCompSocialRules::SocialRules::_iceReadImpl(::Ice::InputStream* istr)
{
    istr->startSlice();
    ::Ice::StreamReader< SocialRules, ::Ice::InputStream>::read(istr, *this);
    istr->endSlice();
}
/// \endcond

/// \cond INTERNAL
void
RoboCompSocialRules::_icePatchObjectPtr(SocialRulesPtr& handle, const ::Ice::ObjectPtr& v)
{
    handle = SocialRulesPtr::dynamicCast(v);
    if(v && !handle)
    {
        IceInternal::Ex::throwUOE(SocialRules::ice_staticId(), v);
    }
}
/// \endcond

namespace Ice
{
}

#endif
